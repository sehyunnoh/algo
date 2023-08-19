import Hello from './component/Hello'
import style from './App.module.css'

function App() {
  return (
    <div className="App">
      <Hello/>
      <div className={style.box}></div>
    </div>
  );
}

export default App;
