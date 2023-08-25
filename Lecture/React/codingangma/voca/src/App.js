import Header from "./component/Header";
import DayList from "./component/DayList";
import Day from "./component/Day";
import { BrowserRouter, Route, Switch } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
    <div className="App">
      <Header />
      <Switch>
        <Route exact path="/">
          <DayList />
        </Route>
        <Route path="/day">
          <Day day={1}/>
        </Route>
      </Switch>
    </div>
    </BrowserRouter>
  );
}

export default App;
