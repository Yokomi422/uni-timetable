'use client';
import React, { useState } from 'react';

export default function Search() {
  const [selectedYear, setSelectedYear] = useState('2024年度');
  const [selectedGrade, setSelectedGrade] = useState('1');
  const [selectedSemester, setSelectedSemester] = useState('S');
  const [keyword, setKeyword] = useState('');

  const handleYearChange = (year: string) => {
    setSelectedYear(year);
  };

  const handleGradeChange = (grade: string) => {
    setSelectedGrade(grade);
  };

  const handleSemesterChange = (semester: string) => {
    setSelectedSemester(semester);
  };

  const handleKeywordChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setKeyword(event.target.value);
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="mb-4 text-center text-4xl font-bold">授業検索</h1>

      <div className="mb-8">
        <h2 className="text-2xl font-bold">年度</h2>
        <div className="mt-4 flex space-x-4">
          <button
            className={`rounded-lg px-4 py-2 ${
              selectedYear === '2024年度' ? 'bg-blue-500 text-white' : 'bg-gray-200'
            }`}
            onClick={() => handleYearChange('2024年度')}
          >
            2024年度
          </button>
          <button
            className={`rounded-lg px-4 py-2 ${
              selectedYear === '2023年度' ? 'bg-blue-500 text-white' : 'bg-gray-200'
            }`}
            onClick={() => handleYearChange('2023年度')}
          >
            2023年度
          </button>
        </div>
      </div>

      <div className="mb-8">
        <h2 className="text-2xl font-bold">学年</h2>
        <div className="mt-4 flex space-x-4">
          {['すべて', '1', '2', '3', '4', '5', '6'].map((grade) => (
            <button
              key={grade}
              className={`rounded-lg px-4 py-2 ${
                selectedGrade === grade ? 'bg-green-500 text-white' : 'bg-gray-200'
              }`}
              onClick={() => handleGradeChange(grade)}
            >
              {grade}
            </button>
          ))}
        </div>
      </div>

      <div className="mb-8">
        <h2 className="text-2xl font-bold">開講時期</h2>
        <div className="mt-4 flex space-x-4">
          {['通年', 'S', 'A'].map((semester) => (
            <button
              key={semester}
              className={`rounded-lg px-4 py-2 ${
                selectedSemester === semester ? 'bg-yellow-500 text-white' : 'bg-gray-200'
              }`}
              onClick={() => handleSemesterChange(semester)}
            >
              {semester}
            </button>
          ))}
        </div>
      </div>

      <div className="mb-8">
        <h2 className="text-2xl font-bold">キーワード検索</h2>
        <input
          type="text"
          className="mt-4 w-full rounded-lg border-2 p-2"
          placeholder="キーワードを入力"
          value={keyword}
          onChange={handleKeywordChange}
        />
      </div>
    </div>
  );
}
