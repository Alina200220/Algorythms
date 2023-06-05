import React, { useState,useEffect } from 'react';


function App() {

  const [data, setData]=useState();
  const[array,setArray]=useState();
    const handleSubmit=(event)=>{
        const formData=new FormData(event.target)
        fetch('http://127.0.0.1:8000/sort/search/', {
        method: 'POST',
        body: formData,})
    }
      useEffect(() => {
         fetch('http://127.0.0.1:8000/sort/search/')
           .then((response) => {
             if (!response.ok) {
               throw new Error(
                 `This is an HTTP error: The status is ${response.status}`
               );
             }
             return response.json();
           })
           .then((response) => setData(response))
          
           .catch((err) => {
             console.log(err.message);
           });
       }, []);
       useEffect(() => {
        fetch('http://127.0.0.1:8000/sort/search/get')
          .then((response) => {
            if (!response.ok) {
              throw new Error(
                `This is an HTTP error: The status is ${response.status}`
              );
            }
            return response.json();
          })
          .then((response) => setArray(response))
         
          .catch((err) => {
            console.log(err.message);
          });
      }, []);
      

  return (
    <div>
      <div ><p style={{WebkitTextFillColor:'white',textAlign:'center',marginTop:'50px',fontSize:'40px',marginRight:'50px',fontFamily:'courier'}}>Алгоритм тернарного поиска</p></div>
        <form  id="form"  className="row g-3 position-absolute top-50 start-50 translate-middle" style={{marginTop:"30px", borderWidth:'8px',borderColor: '#bc13fe', borderStyle: 'solid',borderRadius:'10px', backgroundColor:'white',width:'700px'}} onSubmit={handleSubmit} >
            <h3 style={{textAlign:'center'}}>Введите массив и искомый элемент</h3>

          <p></p>
            {/* время до метро */}
            <div class="col-md-12" >
                <input name='array' type="text" class="form-control" id="array" placeholder="Массив" required />
            </div>
            <p></p>

            {/* год постройки */}
            <div class="col-md-12">
                <input name='n' type="text" class="form-control" id="n" placeholder="Элемент" required />
            </div>

            <p></p>
            <div className="d-grid gap-2 mx-auto " style={{width:'300px'}} >
                <button type="submit" class="btn btn-outline-dark" > Отправить </button>
            </div>
                <p style={{textAlign:'center',fontSize:'18px'}}>Индекс элемента: {data}</p>     
        </form>
        
        {/*<h4 style={{textDecorationColor:'white'}}>{JSON.stringify(array)}</h4>*/}
       
      </div>
        
        
       
        
      
  );
}

export default App;
