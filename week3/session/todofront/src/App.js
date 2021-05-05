import './App.css';
import React,{useState,useEffect,useRef} from 'react';
import axios from 'axios'

function App() {
  const [todos, setTodos] = useState([])

  useEffect( () => {
    axios.get("http://localhost:8000/select/").then((res) => {
      console.log(res.data)
      setTodos(res.data)
  })
  }, [])

  async function deleteRow(idx){
    const form = new FormData();
    form.append('id',idx)
    axios.post("http://localhost:8000/delete/",form).then((res) => {
      console.log(res.data)
      axios.get("http://localhost:8000/select/").then((res) => {
        console.log(res.data)
        setTodos(res.data)
      })
    })
  }

  async function insert(e){
    if (e.key === "Enter") {
      const form = new FormData();
      // console.log(e.target.value);
      form.append('mainText',e.target.value)
      axios.post("http://localhost:8000/insert/",form).then((res) => {
        console.log(res.data)
        axios.get("http://localhost:8000/select/").then((res) => {
          console.log(res.data)
          setTodos(res.data)
        })
      })
    }
  }

  async function update(idx){
    const form = new FormData();
    form.append('id',idx)
    axios.post("http://localhost:8000/update/",form).then((res) => {
      console.log(res.data)
      axios.get("http://localhost:8000/select/").then((res) => {
        console.log(res.data)
        setTodos(res.data)
      })
    })
  }

  return (
    <div>
      {todos.length > 0 && todos.map((each) => {
        return (
          <div key={each[0]} style={{width:'400px', display:'flex'}}>
            <span style={{marginLeft:'20px'}}>{each[1]}</span> <span style={{marginLeft:'20px'}}>{each[2]}</span><span style={{marginLeft:'20px'}}>{each[3]?
            (<>
            <span className="material-icons">done </span>
            <button key={each[0]} style={{marginLeft:'20px'}} onClick={()=>update(each[0])}>취소</button>
            </>):
            (<>
            <span className="material-icons">close</span>  
            <button key={each[0]} style={{marginLeft:'20px'}} onClick={()=>update(each[0])}>완료</button>
            </>)}
            </span>
          
            <button key={each[0]} style={{marginLeft:'20px'}} onClick={()=>deleteRow(each[0])}>삭제</button>
           
         </div>
        )
    })}
    <input style={{marginLeft:'20px'}} placeholder="일정명" onKeyPress={insert}></input>
    </div>
  );
}

export default App;
