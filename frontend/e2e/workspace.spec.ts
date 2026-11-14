import {expect,test} from '@playwright/test'

test('research workspace, answer detail, and responsive navigation',async({page,isMobile})=>{
  const question='What is the evidence for GLP-1 receptor agonists in obesity treatment?'
  const article={pmid:'123',title:'Synthetic browser test record',year:2024,authors:['Test Author'],journal:'Test Journal',date:'2024',doi:'',abstract:'Synthetic abstract for browser tests only.',types:['Review'],url:'https://pubmed.ncbi.nlm.nih.gov/123/'}
  let saved=false
  let asked=false
  const answer=()=>({id:9,question,conversation:7,created:'2026-11-13T00:00:00Z',sources:[article],saved,status:'retrieval_only',model:'',result:{message:'AI generation requires LLM_MODEL and LLM_API_KEY.'},provenance:{}})
  const conversation=()=>({id:7,title:question,updated:'2026-11-13T00:00:00Z',turns:asked?[answer()]:[]})
  await page.route('**/api/**',async route=>{
    const request=route.request()
    const path=new URL(request.url()).pathname
    switch(path){
      case '/api/session/': return route.fulfill({json:{user:{username:'synthetic',first_name:'',last_name:''},csrf:'test'}})
      case '/api/settings/': return route.fulfill({json:{display:'Comfortable'}})
      case '/api/conversations/': return route.fulfill({json:asked?[conversation()]:[]})
      case '/api/conversations/7/': return route.fulfill({json:conversation()})
      case '/api/ask/':
        expect(request.postDataJSON().question).toBe(question)
        asked=true
        return route.fulfill({json:answer()})
      case '/api/answers/9/': return route.fulfill({json:answer()})
      case '/api/answers/9/save/':
        saved=request.method()==='PUT'
        return route.fulfill({json:{saved}})
      case '/api/saved-answers/': return route.fulfill({json:saved?[answer()]:[]})
      default: return route.fulfill({status:404,json:{detail:'Unknown test endpoint'}})
    }
  })
  await page.route('https://fonts.googleapis.com/**', route=>route.abort())
  await page.goto('/')
  await expect(page.getByRole('heading',{name:'Ask a clinical research question'})).toBeVisible()
  await page.getByRole('button',{name:/GLP-1 receptor/}).click()
  await expect(page.getByRole('textbox',{name:'Research question'})).toHaveValue(question)
  await page.getByRole('button',{name:'Ask AI'}).click()
  await expect(page).toHaveURL(/thread\/7/)
  await expect(page.getByText('Retrieval only')).toBeVisible()
  await page.getByRole('link',{name:'View answer and evidence'}).click()
  await expect(page.getByRole('table')).toBeVisible()
  await page.getByText('Synthetic browser test record').click()
  await expect(page.getByText('Synthetic abstract for browser tests only.')).toBeVisible()
  await page.getByRole('button',{name:'Save answer',exact:true}).click()
  await expect(page.getByRole('button',{name:'Unsave answer'})).toBeVisible()
  if(isMobile) await page.getByRole('button',{name:'Open menu'}).click()
  await page.getByRole('link',{name:'Saved Answers'}).click()
  await expect(page.getByRole('link',{name:new RegExp('What is the evidence')})).toBeVisible()
  expect(await page.evaluate(()=>document.documentElement.scrollWidth)).toBeLessThanOrEqual(await page.evaluate(()=>window.innerWidth))
})
