export type User = {username:string; first_name:string; last_name:string}
export type Session = {user:User|null; csrf:string; model?:string}
export type Article = {pmid:string; title:string; authors:string[]; journal:string; date:string; year:number|null; abstract:string; types:string[]; doi:string; url:string; collection?:string}
export type Section = {text:string; status:string; citations:{pmid:string;quote:string}[]}
export type Answer = {id:number; conversation:number; question:string; created:string; status:string; model:string; saved:boolean; sources:Article[]; result:{message?:string;sections?:Section[]};provenance:{intent?:string; searches?:{query:string;pmids:string[]}[]}}
export type Thread = {id:number; title:string; updated:string; turns?:Answer[]}
export type Preferences = {language:string; detail:string; display:string}

let token = ''
export async function api<T>(path:string, method='GET', body?:unknown):Promise<T> {
  const response = await fetch('/api/'+path, {method, headers:{Accept:'application/json','Content-Type':'application/json','X-CSRFToken':token},body:body===undefined?undefined:JSON.stringify(body)})
  if(response.status===204) return undefined as T
  const data = await response.json().catch(()=>null)
  if (!response.ok) {
    const message = data?.detail || (data && Object.entries(data).map(([k,v])=>k+': '+String(v)).join(' '))
    throw new Error(message || 'Request failed ('+response.status+').')
  }
  if(data?.csrf) token=data.csrf
  return data
}
export function date(value:string) {
  return new Intl.DateTimeFormat(undefined,{dateStyle:'medium'}).format(new Date(value))
}
