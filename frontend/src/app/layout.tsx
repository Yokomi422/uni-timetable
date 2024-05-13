import React from 'react';
import Link from 'next/link';
import { FaHome, FaCalendarAlt, FaSearch, FaUserCircle } from 'react-icons/fa';
import './globals.css';

const Layout = ({ children }: Readonly<{ children: React.ReactNode }>) => {
  return (
    <html lang="ja">
      <body>
        <div className="flex min-h-screen flex-col">
          <main className="container mx-auto flex-grow px-4 py-8">{children}</main>
          <nav className="fixed bottom-0 left-0 right-0 flex items-center justify-around bg-white py-4 shadow-md">
            <Link href="/">
              <div className="flex flex-col items-center space-y-1 text-gray-600 hover:text-blue-500">
                <FaHome className="text-2xl" />
                <span className="text-xs">Home</span>
              </div>
            </Link>
            <Link href="/timetable">
              <div className="flex flex-col items-center space-y-1 text-gray-600 hover:text-blue-500">
                <FaCalendarAlt className="text-2xl" />
                <span className="text-xs">Timetable</span>
              </div>
            </Link>
            <Link href="/search">
              <div className="flex flex-col items-center space-y-1 text-gray-600 hover:text-blue-500">
                <FaSearch className="text-2xl" />
                <span className="text-xs">Search</span>
              </div>
            </Link>
            <Link href="/profile">
              <div className="flex flex-col items-center space-y-1 text-gray-600 hover:text-blue-500">
                <FaUserCircle className="text-2xl" />
                <span className="text-xs">Profile</span>
              </div>
            </Link>
          </nav>
        </div>
      </body>
    </html>
  );
};

export default Layout;
