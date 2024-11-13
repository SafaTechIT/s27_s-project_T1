import React from 'react';
import { Link } from 'react-router-dom';
import './Profile.css';

function Profile() {
    return (
        <div className="profile">
            <Header />
            <div className="content">
                <Sidebar />
                <ProfileDetails />
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
function ProfileDetails() {
    const user = {
        name: " صفا27",
        username: "@salman Farsi",
        bio: "یا امیرالمومنین",
        tweets: 120,
        followers: "1M",
        following: 1438,
    };

    return (
        <main className="profile-details">
            <div className="user-info">
                <img src="https://uploadkon.ir/uploads/31f310_24oizO93EUBNrO.jpg" alt="Banner" className="banner-image" />
                <img src="https://uploadkon.ir/uploads/313610_24تایپوگرافی-2-لوگو-گروه-فیروزه-ای-png.jpeg" alt="Profile" className="profile-image" />
                <h2>{user.name}</h2>
                <p>{user.username}</p>
                <p>{user.bio}</p>
                <div className="stats">
                    <span>{user.tweets} Tweets</span>
                    <span>{user.followers} Followers</span>
                    <span>{user.following} Following</span>
                </div>
            </div>
            <h3>Tweets</h3>
            <TweetList />
        </main>
    );
}

function TweetList() {
    const tweets = [
        { id: 1, content: 'This is my first tweet!' },
        { id: 2, content: 'Hello, Twitter world!' },
        { id: 3, content: 'React is awesome!' },
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

export default Profile;