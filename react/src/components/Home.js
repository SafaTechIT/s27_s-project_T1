import React from 'react';
import './Home.css';
import { Link } from 'react-router-dom';
function App() {
    return (
        <div className="app">
            <Header />
            <div className="content">
                <Sidebar />
                <MainFeed />
            </div>
        </div>
    );
}

function Header() {
    return (
        <header className="header">
            <div className="header-container">
                <div className="logo">TS</div> {/* لوگو TS */}
                <h1 className="header-title">توییتر سلمان</h1> {/* عنوان هدر */}
            </div>
        </header>
    );
}

function Sidebar() {
    return (
        <aside className="sidebar">
            <div className="logo-container">
                <div className="logo">TS</div> {/* لوگو TS */}
                <h2 className="logo-text">توییتر سلمان</h2> {/* نام توییتر سلمان */}
            </div>
            <ul>
                <li><Link to="/">خانه</Link></li>
                <li><Link to="/explore">اکسپلور</Link></li>
                <li><Link to="/notifications">اعلانها</Link></li>
                <li><Link to="/messages">پیامها</Link></li>
                <li><Link to="/profile">پروفایل</Link></li>
            </ul>
        </aside>
    );
}

function MainFeed() {
    return (
        <main className="main-feed">
            <h2>توییت ها</h2>
            <TweetInput />
            <TweetList />
        </main>
    );
}

function TweetInput() {
    return (
        <div className="tweet-input">
            <textarea placeholder="چه خبر؟ " />
            <button>توییت</button>
        </div>
    );
}

function TweetList() {
    const tweets = [
        { id: 1, content: '!اولین توییت' },
        { id: 2, content: 'Hello Twitter!' },
    ];

    return (
        <div className="tweet-list">
            {tweets.map((tweet) => (
                <div key={tweet.id} className="tweet">
                    {tweet.content}
                </div>
            ))}
        </div>
    );
}

export default App;