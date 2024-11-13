import React from 'react';
import { Link } from 'react-router-dom';
import './Explore.css';
function Explore() {
    return (
        <div className="explore">
            <Header />
            <div className="content">
                <Sidebar />
                <ExploreFeed />
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

function ExploreFeed() {
    const trendingTopics = [
        { id: 1, topic: '#ReactJS', tweets: 1200 },
        { id: 2, topic: '#JavaScript', tweets: 1500 },
        { id: 3, topic: '#WebDevelopment', tweets: 800 },
    ];

    return (
        <main className="explore-feed">
            <h2>اکسپلور</h2>
            <h3>موضوع های داغ</h3>
            <ul className="trending-topics">
                {trendingTopics.map((topic) => (
                    <li key={topic.id} className="topic">
                        {topic.topic} - {topic.tweets} Tweets
                    </li>
                ))}
            </ul>
        </main>
    );
}

export default Explore;