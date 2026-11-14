import {afterEach,describe,expect,it,vi} from 'vitest'
import {cleanup,fireEvent,render,screen} from '@testing-library/react'
import {Composer} from './app'

afterEach(cleanup)
describe('Composer',()=>{
  it('submits with Enter and leaves Shift+Enter and composition available',()=>{
    const send=vi.fn()
    render(<Composer question="A research question" change={vi.fn()} submit={send} busy={false}/>)
    const input=screen.getByRole('textbox',{name:'Research question'})
    fireEvent.keyDown(input,{key:'Enter',shiftKey:true})
    fireEvent.keyDown(input,{key:'Enter',isComposing:true})
    expect(send).not.toHaveBeenCalled()
    fireEvent.keyDown(input,{key:'Enter'})
    expect(send).toHaveBeenCalledTimes(1)
    fireEvent.click(screen.getByRole('button',{name:'Ask AI'}))
    expect(send).toHaveBeenCalledTimes(2)
  })
  it('blocks submission when pending or invalid',()=>{
    const send=vi.fn()
    const props={question:'yes',change:vi.fn(),submit:send}
    const view=render(<Composer {...props} busy={false}/>)
    fireEvent.keyDown(screen.getByRole('textbox'),{key:'Enter'})
    view.rerender(<Composer {...props} question="Enough characters" busy follow/>)
    fireEvent.keyDown(screen.getByRole('textbox',{name:'Follow-up question'}),{key:'Enter'})
    expect(send).not.toHaveBeenCalled()
  })
})
