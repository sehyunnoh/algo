// const Hello = () =>  {
//   <p>Hello</p>
// }

// export default Hello;
import styles from "./Hello.module.css"

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
    <div className={styles.box}>Hello</div>
  </>
}