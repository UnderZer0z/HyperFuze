import './Home.css';
import player from '../img/player.png'
import gun from '../img/gun.png'
import blob from '../img/blob.svg'
import discordLogo from '../img/discord.svg'
import youtube from '../img/youtube.svg'

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

            <img src={blob} alt="blob" />

            <div className="blobtext">

              <h2>היצטרפו עכשיו!</h2>
              <img src={discordLogo} alt="discord" />
              <h3>הרשמה בעזרת</h3>
              <h3>חשבון הדיסקורד</h3>

            </div>

          </div>

      </div>

      <div className="info"> 
        <h1>קצת מידע על הקהילה</h1>
        <p>
        הייפר-פיוז היא קהילת גיימינג דמוקרטית המאפשרת לשחקנים לבחור את הכיון אליה
        הקהילה מתקדמת ולשמור על איכות המשחק גבוהה. כל שבוע מתקיימים שני אירועי
        גיימינג במשחקים  אשר הקהילה קבועת. הקהילה גם מחזיקה שרתים אשר פתוחים
        24/7 לכל הקהילה. 
        </p>

        <div className="community-highlight">
          <div className="vid">
            <img src={youtube} alt="youtube"/>
          </div>
        </div>

      </div>


      </div>


    <div className="events">

    </div>


    </section>
  );

}

export default Home;
