## keyword
> `create-react-app`, `functional component`, `jsx`, `useState`, `useEffect`, `react hook`, `json-server`, `rest api`, `CRUD`

```js
npx create-react-app voca // if we use npx, we don't need to install create-react-app (npm에 있는 package를 바로 실행 시켜줌)
npm start
```

- HMR(Hot Module Replacement): 코드 수정 되었을때 바로 update 됨.

- react로 만들어진 페이지는 component 단위로 만들어져 있음. component를 각각 만들어서 조립.
- 코드 재사용, 유지보수 용이함.

## JSX(JavaScript XAML)
- setup autocomplete at settings.json
```
 "emmet.includeLanguages": {
     "javascript": "javascriptreact"
 },
 "emmet.syntaxProfiles": {
     "javascript": "jsx"
 }
```

## Component
- component는 대문자로 시작해야 함.
- component는 하나의 태그로 감싸져 있어야 함.
- component는 재사용 가능한 UI 조각이다.
- component는 props를 통해 데이터, 이벤트를 전달 받을 수 있다.
- component는 state를 가질 수 있다.
- component는 JSX를 반환한다.
- component는 자신의 state를 변경할 수 없다.
- component는 자신의 props를 변경할 수 없다.
- component는 자신의 state를 변경할 수 없다.
```js
const Hello = () => {
  return <h1>Hello</h1>
}

export default Hello
```

```js
export default function Hello() {
  return <h1>Hello</h1>
}
```
  
```js
<Hello />
<Hello></Hello>

```

## CSS
```js
// inline (추천하지 않음.)
export default function Hello() {
  return <>
    <h1 style={{ 
      color: "blue", 
      borderRight: '12px solid #000',
      marginBottom: "50px",
      opacity: 0.5
    }}>
      Hello
    </h1>
    <World />
  </>
}

// use.index.css, App.css
// 공통 적용되고, over write 적용 됨.

// component별로 개별적으로 스타일 적용
import styles from './Hello.module.css'

<div className={styles.box}></div>

```



## 이벤트 처리

```js
onClick
onChange
```

## state
- component 별로 각각 관리된다.
```js
import {useState} from "react"

//const [state, setState] = useState(initialState)
const[name, setName] = useState("Mike")

function changeName() {
  setName( name === "Mike"?"Jane":"Mike")
}
```

## props
- component에서 component로 전달되는 데이터
- props는 읽기 전용이다. (값을 변경할수 없다.)
- 
```js
<Hello age={10}>
```
```js
export default function Hello(props) {
  const [age, setAge] = useState(props.age)

  return <h1>Hello {props.age}</h1>
}

export default function Hello({age}) {
  const msg = age > 19 ? "성인입니다." : "미성년자입니다."

  return <h1>Hello {props.age}</h1>
}

```

## dummy 데이터 구현
-[code](https://github.com/coding-angma/voca)
```js
data.json

import dummy from "../db/data.json"
```
## react-router-dom
```js
npm install react-router-dom

import {BrowserRouter, Route, Link} from "react-router-dom"


function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <Header />
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/day/:day">
            <Day />
          </Route>
          <Route>
            <EmptyPage />
          </Route>
        </Switch>
      </div>
    </BrowserRouter>
  )
}

```

```js
import { useParams } from "react-router-dom"

export default function Day() {
  const { day } = useParams()
}

```

```js
import {Link} from "react-router-dom"
<Link to={`/day/${day.day}`}>
```

## json-server
```bash 
npm install -g json-server
json-server --watch ./src/db/data.json --port 3001
```

## useEffect, fetch
- component 시작할때, 업데이트 될때, 사라질때 호출 됨.
```js
import {useEffect, useState} from "react"

// 의존성 배열 (count가 변경될때만 호출 됨.)
useEffect(() => {}, [count]);

// 의존성 배열에 빈 배열을 넣으면, 처음에만 호출 됨.
useEffect(() => {
  fetch(`http://localhost:3001/posts`)
    .then(res => {
      return res.json()
    })
    .then(data => {
      setDays(data)
    })
}, []);
```

## Custom Hooks

## CRUD

## useRef, useHistory
- useRef: DOM에 접근할때 사용
- useHistory: 페이지 이동할때 사용
- useLocation: 현재 페이지 정보를 알고 싶을때 사용
- useParams: url에 있는 parameter를 가져올때 사용
- useRouteMatch: 현재 url과 매치되는 정보를 알고 싶을때 사용
- usePrompt: 페이지 이동시 경고창을 띄우고 싶을때 사용
- useConfirm: 버튼 클릭시 경고창을 띄우고 싶을때 사용
- usePreventLeave: 페이지를 벗어날때 경고창을 띄우고 싶을때 사용
- useBeforeLeave: 마우스가 페이지를 벗어날때 경고창을 띄우고 싶을때 사용
- useFadeIn: 페이지가 로딩될때 fade in 효과를 주고 싶을때 사용
- useNetwork: 네트워크 상태를 알고 싶을때 사용
- useScroll: 스크롤 위치를 알고 싶을때 사용
- useFullscreen: 특정 element를 전체화면으로 보여주고 싶을때 사용
- useNotification: 브라우저 알림을 사용하고 싶을때 사용
- useAxios: axios를 사용하고 싶을때 사용
- useClick: 특정 element를 클릭하고 싶을때 사용
  

```js
import {useHistory} from "react-router-dom"

history.push(`/day/${day.day}`)
```

## typescript 적용