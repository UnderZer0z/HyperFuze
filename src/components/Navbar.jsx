import './Navbar.css';

function Navbar() {
  return (
    <header>
        <h1>Hyper<b>Fuze</b></h1>
        <nav>
            <a className='reg' href="/reg">הירשם</a>
            <a href="/game">משחקים</a>
            <a href="/server">שרתים</a>
            <a href="/news">חדשות</a>
        </nav>
    </header>
  );
}

export default Navbar;
