import { useState, useEffect } from 'react'

export const ToDo = () => {

  const [task, setTask] = useState([])
  const [dato, setDato] = useState()

  const getTask = async () => {
    const data = await fetch(process.env.REACT_APP_URL_API)
    const task = await data.json()
    setTask(task)
  }

  const newTask = async (event) => {
    event.preventDefault()
    await fetch(process.env.REACT_APP_URL_API, {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        task: dato,
      })
    });
    getTask()
    setDato('')
    event.target.reset()
  }

  const completeTask = async (id) => {
    await fetch(`${process.env.REACT_APP_URL_API}/checked/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        task: dato,
      })
    });
    getTask()
  }
  

  useEffect(() => {
    getTask()
  }, [])

    return (
      <div id="CenterToDo">
        <div id="ToDo">
        <form onSubmit={newTask}> 
          <input type="text" placeholder="Add new Task" name="task" 
          vale = {dato}
          onChange = {event => setDato(event.target.value)}
          autoFocus
          />
          <input type="submit" value="Add" />
        </form>
        <ul>
          {task.map(item => {
            if (item.state === 0)
              return <li key={item.id}>
                  <button value={item.id} onClick={event => completeTask(event.target.value)}>{item.task}</button>
                </li>
            })}
        </ul>
      </div>
      </div>
      
    );
  };