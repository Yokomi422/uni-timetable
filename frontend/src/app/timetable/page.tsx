'use client';

import React, { useState } from 'react';
import Link from 'next/link';

export default function Timetable() {
  const [selectedYear, setSelectedYear] = useState('2024年度');
  const [selectedSemester, setSelectedSemester] = useState('S');

  const handleYearChange = (year: string) => {
    setSelectedYear(year);
  };

  const handleSemesterChange = (semester: string) => {
    setSelectedSemester(semester);
  };

  const classes = {
    '1': {
      Mon: { name: '数学', teacher: '山田 太郎', link: '/details/math' },
      Tue: { name: '英語', teacher: '佐藤 花子', link: '/details/english' },
    },
    '2': {
      Mon: { name: '物理', teacher: '田中 一郎', link: '/details/physics' },
      Wed: { name: '生物', teacher: '鈴木 次郎', link: '/details/biology' },
    },
    '3': {
      Tue: { name: '化学', teacher: '加藤 花子', link: '/details/chemistry' },
      Thu: { name: '体育', teacher: '佐々木 三郎', link: '/details/pe' },
    },
    '4': {
      Wed: { name: '歴史', teacher: '中村 四郎', link: '/details/history' },
      Fri: { name: '美術', teacher: '伊藤 五郎', link: '/details/art' },
    },
    '5': { Thu: { name: '音楽', teacher: '小林 六郎', link: '/details/music' } },
    '6': { Fri: { name: '地理', teacher: '斉藤 七郎', link: '/details/geography' } },
  };

  return (
    <div className="w-full px-4 py-8">
      <h1 className="mb-4 text-center text-4xl font-bold">時間割</h1>

      <div className="mb-8 flex justify-center space-x-8">
        <div>
          <h2 className="text-2xl font-bold">年度</h2>
          <div className="mt-4 flex space-x-4">
            <button
              className={`rounded-lg px-4 py-2 ${selectedYear === '2024年度' ? 'bg-blue-500 text-white' : 'bg-gray-200'}`}
              onClick={() => handleYearChange('2024年度')}
            >
              2024年度
            </button>
            <button
              className={`rounded-lg px-4 py-2 ${selectedYear === '2023年度' ? 'bg-blue-500 text-white' : 'bg-gray-200'}`}
              onClick={() => handleYearChange('2023年度')}
            >
              2023年度
            </button>
          </div>
        </div>

        <div>
          <h2 className="text-2xl font-bold">開講時期</h2>
          <div className="mt-4 flex space-x-4">
            <button
              className={`rounded-lg px-4 py-2 ${selectedSemester === 'S' ? 'bg-green-500 text-white' : 'bg-gray-200'}`}
              onClick={() => handleSemesterChange('S')}
            >
              S
            </button>
            <button
              className={`rounded-lg px-4 py-2 ${selectedSemester === 'A' ? 'bg-green-500 text-white' : 'bg-gray-200'}`}
              onClick={() => handleSemesterChange('A')}
            >
              A
            </button>
          </div>
        </div>
      </div>

      <div className="overflow-x-auto">
        <table className="w-full border-collapse border border-gray-300 text-lg">
          <thead>
            <tr>
              <th className="border border-gray-300 px-6 py-3">時間</th>
              <th className="border border-gray-300 px-6 py-3">月曜日</th>
              <th className="border border-gray-300 px-6 py-3">火曜日</th>
              <th className="border border-gray-300 px-6 py-3">水曜日</th>
              <th className="border border-gray-300 px-6 py-3">木曜日</th>
              <th className="border border-gray-300 px-6 py-3">金曜日</th>
            </tr>
          </thead>
          <tbody>
            {['1', '2', '3', '4', '5', '6'].map((period) => (
              <tr key={period}>
                <td className="border border-gray-300 px-6 py-3">{period}限</td>
                {['Mon', 'Tue', 'Wed', 'Thu', 'Fri'].map((day) => (
                  <td key={day} className="border border-gray-300 px-6 py-3">
                    {classes[period][day] ? (
                      <>
                        <Link href={classes[period][day].link}>
                          <div className="block rounded-md bg-gray-200 p-2 text-center font-bold text-blue-500 hover:bg-gray-300">
                            {classes[period][day].name}
                          </div>
                        </Link>
                        <hr className="my-2 border-t-2 border-gray-300" />
                        <div className="text-center text-sm">{classes[period][day].teacher}</div>
                      </>
                    ) : (
                      ''
                    )}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
