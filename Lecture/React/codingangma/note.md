## keyword
> `create-react-app`, `functional component`, `jsx`, `useState`, `useEffect`, `react hook`, `json-server`, `rest api`, `CRUD`

```js
npx create-react-app voca
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

## CSS
```
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
공통 적용되고, over write 적용 됨.

// component별로 개별적으로 스타일 적용
import styles from './Hello.module.css

<div className={styles.box}></div>

```

## 이벤트 처리

## state

## props

## react-router-dom
```
npm install react-router-dom
```

## json-server

## useEffect, fetch

## Custom Hooks