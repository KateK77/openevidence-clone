import {expect,test,type Page} from '@playwright/test'

const question='What is the evidence for GLP-1 receptor agonists in obesity treatment?'
async function fixture(page:Page){
  const article={pmid:'123',title:'Synthetic browser test record',year:2024,authors:['Test Author'],journal:'Test Journal',date:'2024',electronic_date:'2024 01 01',issue_date:'2024 Feb',doi:'',abstract:'Synthetic abstract for browser tests only.',types:['Review'],url:'https://pubmed.ncbi.nlm.nih.gov/123/'}
  const state={saved:false,publication:false,collection:'',asked:false,title:question,question,user:{username:'synthetic',first_name:'',last_name:''} as {username:string;first_name:string;last_name:string}|null,preferences:{language:'English',detail:'Standard',display:'Comfortable'},saves:0,failSave:false,searches:[] as {id:number;filters:Record<string,string>}[]}
  const answer=()=>({id:9,question:state.question,conversation:7,created:'2026-11-13T00:00:00Z',sources:[article],saved:state.saved,status:'retrieval_only',model:'',result:{message:'Publications retrieved. AI synthesis is not configured.'},provenance:{pipeline_version:'round-02',intent:'evidence review',normalization:{original:state.question,normalized:'diabetes treatment',method:'Chinese terminology glossary',notice:'Review the query mapping.'},searches:[{query:'diabetes treatment',pmids:['123']}]}})
  const conversation=()=>({id:7,title:state.title,updated:'2026-11-13T00:00:00Z',turns:state.asked?[answer()]:[]})
  await page.route('**/api/**',async route=>{
    const request=route.request();const path=new URL(request.url()).pathname;const method=request.method()
    switch(path){
      case '/api/session/': return route.fulfill({json:{user:state.user,csrf:'test',generation_configured:false}})
      case '/api/login/': state.user={username:'synthetic',first_name:'',last_name:''};return route.fulfill({json:{user:state.user,csrf:'test'}})
      case '/api/logout/': state.user=null;return route.fulfill({json:{user:null,csrf:'test'}})
      case '/api/profile/': Object.assign(state.user!,request.postDataJSON());return route.fulfill({json:state.user})
      case '/api/settings/':
        if(method==='PATCH'){state.saves++;if(state.failSave)return route.fulfill({status:503,json:{detail:'Synthetic save failure'}});Object.assign(state.preferences,request.postDataJSON())}
        return route.fulfill({json:state.preferences})
      case '/api/conversations/': return route.fulfill({json:state.asked?[conversation()]:[]})
      case '/api/conversations/7/':
        if(method==='PATCH')state.title=request.postDataJSON().title
        return route.fulfill({json:conversation()})
      case '/api/ask/': state.asked=true;state.question=request.postDataJSON().question;return route.fulfill({json:answer()})
      case '/api/answers/9/': return route.fulfill({json:answer()})
      case '/api/answers/9/save/': state.saved=method==='PUT';state.saves++;return route.fulfill({json:{saved:state.saved}})
      case '/api/saved-answers/': return route.fulfill({json:state.saved?[answer()]:[]})
      case '/api/articles/': return route.fulfill({json:[article]})
      case '/api/articles/123/save/': state.publication=method==='PUT';if(state.publication)state.collection=request.postDataJSON().collection;return route.fulfill({json:{saved:state.publication}})
      case '/api/saved-articles/': return route.fulfill({json:state.publication?[{...article,collection:state.collection}]:[]})
      case '/api/saved-searches/': if(method==='POST'){state.searches.push({id:1,filters:request.postDataJSON()});return route.fulfill({json:state.searches[0]})}return route.fulfill({json:state.searches})
      default: return route.fulfill({status:404,json:{detail:'Unknown synthetic test endpoint'}})
    }
  })
  return state
}
async function navigate(page:Page,isMobile:boolean,name:string){
  if(isMobile)await page.getByRole('button',{name:'Open menu'}).click()
  await page.getByRole('navigation').getByRole('link',{name,exact:true}).click()
}
test('research, evidence, saved feedback and responsive navigation',async({page,isMobile})=>{
  await fixture(page);await page.goto('/')
  await expect(page.getByRole('heading',{name:/Better questions/})).toBeVisible()
  await page.getByRole('button',{name:/GLP-1 & weight/}).click()
  await expect(page.getByRole('textbox',{name:'Research question'})).toHaveValue(question)
  await page.getByRole('button',{name:'Ask AI'}).click()
  await expect(page).toHaveURL(/thread\/7/)
  await expect(page.getByText('Literature only')).toBeVisible()
  await page.getByRole('link',{name:'View answer and evidence'}).click()
  await page.getByText('Abstract & publication details',{exact:true}).click()
  await expect(page.getByText('Synthetic abstract for browser tests only.')).toBeVisible()
  await expect(page.getByText('Electronic publication',{exact:true})).toBeVisible()
  await page.getByRole('button',{name:'Save answer',exact:true}).click()
  await expect(page.getByRole('button',{name:'Saved',exact:true})).toBeDisabled()
  await expect(page.getByRole('status')).toContainText('Answer saved')
  await navigate(page,isMobile,'Saved answers')
  await expect(page.getByRole('link',{name:new RegExp('What is the evidence')})).toBeVisible()
  expect(await page.evaluate(()=>document.documentElement.scrollWidth)).toBeLessThanOrEqual(await page.evaluate(()=>innerWidth))
})
test('short Chinese and English questions are submitted',async({page})=>{
  const state=await fixture(page)
  for(const input of ['糖尿病','pain']){
    await page.goto('/')
    await page.getByRole('textbox',{name:'Research question'}).fill(input)
    await expect(page.getByRole('button',{name:'Ask AI'})).toBeEnabled()
    await page.getByRole('button',{name:'Ask AI'}).click()
    await expect(page).toHaveURL(/thread\/7/)
    expect(state.question).toBe(input)
  }
})
test('settings save is visible, durable, blocks repeats and allows retry',async({page})=>{
  const state=await fixture(page);await page.goto('/settings')
  await expect(page.getByRole('button',{name:'Save preferences'})).toBeDisabled()
  await page.getByLabel('Answer language').selectOption('Chinese')
  await page.getByRole('button',{name:'Save preferences'}).click()
  await expect(page.getByRole('button',{name:'Saved',exact:true})).toBeDisabled()
  await expect(page.getByRole('status')).toHaveText('Changes saved successfully.')
  expect(state.saves).toBe(1)
  await page.reload()
  await expect(page.getByLabel('Answer language')).toHaveValue('Chinese')
  state.failSave=true
  await page.getByLabel('Response detail').selectOption('Detailed')
  await page.getByRole('button',{name:'Save preferences'}).click()
  await expect(page.getByRole('alert')).toContainText('Synthetic save failure')
  await expect(page.getByLabel('Response detail')).toHaveValue('Detailed')
  state.failSave=false
  await page.getByRole('button',{name:'Save preferences'}).click()
  await expect(page.getByRole('button',{name:'Saved',exact:true})).toBeDisabled()
})
test('publication and collection save feedback persists',async({page,isMobile})=>{
  await fixture(page);await page.goto('/library')
  await page.getByLabel('Keywords, PMID or DOI').fill('123')
  await page.getByRole('button',{name:'Search PubMed',exact:true}).click()
  await page.getByRole('button',{name:'Save publication',exact:true}).click()
  await expect(page.getByRole('button',{name:'Saved',exact:true})).toBeDisabled()
  await expect(page.getByRole('status')).toContainText('Publication saved')
  await navigate(page,isMobile,'Saved publications')
  await page.getByRole('textbox',{name:'Collection',exact:true}).fill('Methods')
  await page.getByRole('button',{name:'Update collection'}).click()
  await expect(page.getByText('Changes saved successfully.')).toBeVisible()
  await page.reload()
  await expect(page.getByRole('textbox',{name:'Collection',exact:true})).toHaveValue('Methods')
  await page.getByRole('button',{name:'Remove from library'}).click()
  await expect(page.getByText('No saved publications found')).toBeVisible()
})
test('saved search can be reopened',async({page})=>{
  await fixture(page);await page.goto('/library')
  await page.getByLabel('Keywords, PMID or DOI').fill('diabetes')
  await page.getByLabel('Year',{exact:true}).fill('2021')
  await page.getByRole('button',{name:'Search PubMed',exact:true}).click()
  await page.getByRole('button',{name:'Save this search'}).click()
  await expect(page.getByRole('button',{name:'Search saved'})).toBeDisabled()
  await page.reload()
  await page.getByText('Saved searches (1)',{exact:true}).click()
  await page.getByRole('button',{name:/diabetes.*year/}).click()
  await expect(page.getByLabel('Year',{exact:true})).toHaveValue('2021')
  await expect(page.getByText('Synthetic browser test record')).toBeVisible()
})
test('logout immediately removes identity and protects saved data after reload',async({page})=>{
  await fixture(page);await page.goto('/profile')
  await page.getByRole('button',{name:'Sign out',exact:true}).click()
  await expect(page.getByRole('heading',{name:'Welcome back'})).toBeVisible()
  await expect(page.locator('.account')).toHaveText('Sign in')
  await page.reload()
  await expect(page.getByRole('heading',{name:'Welcome back'})).toBeVisible()
  await page.goto('/saved')
  await expect(page.getByRole('heading',{name:'Your research, in one place'})).toBeVisible()
})
test('small viewport drawer can reach Profile and close with Escape',async({page})=>{
  await fixture(page);await page.setViewportSize({width:390,height:560});await page.goto('/')
  await page.getByRole('button',{name:'Open menu'}).click()
  const profile=page.getByRole('navigation').getByRole('link',{name:'Profile',exact:true})
  await profile.scrollIntoViewIfNeeded();await expect(profile).toBeVisible();await profile.click()
  await expect(page.getByRole('heading',{name:'Your profile'})).toBeVisible()
  await page.getByRole('button',{name:'Open menu'}).click()
  await page.keyboard.press('Escape')
  await expect(page.getByRole('button',{name:'Open menu'})).toHaveAttribute('aria-expanded','false')
  expect(await page.evaluate(()=>document.documentElement.scrollWidth)).toBe(390)
})
