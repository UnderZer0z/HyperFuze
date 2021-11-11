import './App.css';
import Navbar from './components/Navbar';
import Home from './components/Home'
// import Games from './components/Games'
import Footer from './components/Footer';


function App() {
  return (
      
        <div>
          <Navbar/>
          <Home />
          {/* <Games /> */}
          <Footer />
        </div>
      
  );
}

export default App;
