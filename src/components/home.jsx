import './Home.css';
import player from '../img/player.png'
import gun from '../img/gun.png'
import blob from '../img/blob.svg'


function Home() {

  return (
    <section dir='rtl'>

      <div className="tab">

        <div className="heading">

          <img src={player} alt="ops"/>

          <div className="titling">
            <h1>קהילת הייפר-<b>פיוז</b>,<img src={gun} alt="ops"/></h1>
            <h2>כי פה השחקן קובע!</h2>
          </div>

          <div className="discord">
            <img src={blob} />
            {/* <h2>היצטרפו עכשיו!</h2> */}
          </div>

      </div>

      {/* <div className="text"> 
        <h1>קצת מידע על הקהילה</h1>
        <p>
        הייפר-פיוז היא קהילת גיימינג דמוקרטית המאפשרת לשחקנים לבחור את הכיון אליה
        הקהילה מתקדמת ולשמור על איכות המשחק גבוהה. כל שבוע מתקיימים שני אירועי
        גיימינג במשחקים  אשר הקהילה קבועת. הקהילה גם מחזיקה שרתים אשר פתוחים
        24/7 לכל הקהילה. 
        </p>
      </div> */}

      {/* ennd of the tab */}
      </div>


    </section>
  );

}

export default Home;
