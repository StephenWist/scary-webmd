import Image from 'next/image'
import Button from './button'



export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between py-0 px-0 bg-slate-200 text-center">
      <header className='flex-row min-h-max max-w-full min-w-full h-24 bg-blue-100'>
        <h1>Scary-WebMD</h1>
        <h2><em>Hypocondriacs Unite!</em></h2>
      </header>
      <div className='p-24 bg-stone-50'>
        <p>Here's Scary-WebMD where you can draw your own conclusions about your health from peer reviewed medical 
          research based on searching your vague symptoms over genetic variant literature where your query was found within.
        </p>
      </div>
      <form action='' method='post'>
        <div className='bg-slate-300 p-24'>
          <label htmlFor='symptoms'>Describe your symptoms:</label>
          <input type='text' name='symptoms' id='symptoms' required />
          <br/>
          <Button />
        </div>
      </form>
      <div  className='bg-slate-300 w-4/5 h-full py-24'>
        <p>placeholder</p>
      </div>
    </main>
  )
}
