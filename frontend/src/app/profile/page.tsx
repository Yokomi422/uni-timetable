import React from 'react';
import Image from 'next/image';

export default function Profile() {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="mb-4 text-center text-4xl font-bold">Profile</h1>

      <div className="mb-8">
        <h2 className="text-2xl font-bold">アカウント</h2>
        <div className="mt-4 rounded-lg border-2 p-4">
          <Image
            width={96}
            height={96}
            src="/sample.profile.jpeg"
            alt="Profile Picture"
            className="mr-4 inline-block h-24 w-24 rounded-full"
          />
          <div className="inline-block align-middle">
            <h3 className="text-xl font-bold">John Doe</h3>
          </div>
        </div>
      </div>

      <div className="mb-8">
        <h2 className="text-2xl font-bold">あなたの履修状況</h2>
        <div className="mt-4 rounded-lg border-2 p-4">
          <div className="mb-4">
            <h3 className="text-xl font-semibold">必修 (残り: 12 単位)</h3>
            <p className="text-lg">24 単位</p>
          </div>
          <div className="mb-4">
            <h3 className="text-xl font-semibold">限定選択 (残り: 6 単位)</h3>
            <p className="text-lg">18 単位</p>
          </div>
          <div className="mb-4">
            <h3 className="text-xl font-semibold">その他 (残り: 8 単位)</h3>
            <p className="text-lg">12 単位</p>
          </div>
        </div>
      </div>

      <div className="mb-8">
        <h2 className="text-2xl font-bold">必要単位数</h2>
        <p className="text-lg">総必要単位数: 60 単位</p>
      </div>
    </div>
  );
}
