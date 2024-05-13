import React from 'react';
import Link from 'next/link';

export default function Home() {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="mb-4 text-4xl font-bold">Welcome to Your Timetable</h1>
      <p className="mb-8 text-xl">
        Manage your university schedule with ease. Here is how to get started:
      </p>
      <div className="mb-8">
        <h2 className="mb-2 text-2xl font-bold">1. View Your Timetable</h2>
        <p className="mb-4">
          Navigate to the Timetable page to see your current schedule. Here you can view your
          lectures, times, and locations for each day of the week.
        </p>
        <Link href="/timetable">
          <div className="inline-block rounded-lg bg-blue-500 px-4 py-2 text-white hover:bg-blue-600">
            Go to Timetable
          </div>
        </Link>
      </div>
      <div className="mb-8">
        <h2 className="mb-2 text-2xl font-bold">2. Search for Lectures</h2>
        <p className="mb-4">
          Use the Search page to find lectures you want to add to your timetable. You can search by
          course name, professor, or time slot.
        </p>
        <Link href="/search">
          <div className="inline-block rounded-lg bg-green-500 px-4 py-2 text-white hover:bg-green-600">
            Go to Search
          </div>
        </Link>
      </div>
      <div>
        <h2 className="mb-2 text-2xl font-bold">3. Customize Your Profile</h2>
        <p className="mb-4">
          Visit the Profile page to add your personal information and preferences. You can also set
          your default campus and notification settings here.
        </p>
        <Link href="/profile">
          <div className="inline-block rounded-lg bg-yellow-500 px-4 py-2 text-white hover:bg-yellow-600">
            Go to Profile
          </div>
        </Link>
      </div>
    </div>
  );
}
