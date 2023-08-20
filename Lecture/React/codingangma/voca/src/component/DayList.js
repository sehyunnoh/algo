import dummy from '../db/data.json';

export default function DayList() {
  return (
    <ul className="list_day">
      {dummy.days.map(day => (
        <li key={day.id}>
          <span>{day.day} Day</span>
        </li>
      ))}
    </ul>
  )
}