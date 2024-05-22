'use client';
import React, { useState } from 'react';

export default function Search() {
  const [department, setDepartment] = useState('');
  const [day, setDay] = useState('');
  const [period, setPeriod] = useState('');

  const handleDepartmentChange = (event: { target: { value: React.SetStateAction<string>; }; }) => {
    setDepartment(event.target.value);
  };

  const handleDayChange = (event: { target: { value: React.SetStateAction<string>; }; }) => {
    setDay(event.target.value);
  };

  const handlePeriodChange = (event: { target: { value: React.SetStateAction<string>; }; }) => {
    setPeriod(event.target.value);
  };

  const searchClasses = async () => {
    const queryParams = new URLSearchParams({
      department,
      day,
      period
    }).toString();
  
    const url = `http://127.0.0.1:8080/search?${queryParams}`;
  
    const response = await fetch(url, {
      headers: {
        'Accept': 'application/json' 
      }
    });
  
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
  
    const data = await response.json();
    console.log('Response data:', data);
  };
  
  

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="mb-4 text-center text-4xl font-bold">授業検索</h1>

      <div className="mb-8">
        <h2 className="text-2xl font-bold">学科</h2>
        <select
          className="mt-4 w-full rounded-lg border-2 p-2"
          value={department}
          onChange={handleDepartmentChange}
        >
          <option value="">学科を選択</option>
          <option value="計数工学科">計数工学科</option>
          <option value="航空宇宙工学科">航空宇宙工学科</option>
        </select>
      </div>

      <div className="mb-8">
        <h2 className="text-2xl font-bold">曜日</h2>
        <select
          className="mt-4 w-full rounded-lg border-2 p-2"
          value={day}
          onChange={handleDayChange}
        >
          <option value="">曜日を選択</option>
          {['月', '火', '水', '木', '金'].map((day) => (
            <option key={day} value={day}>
              {day}曜日
            </option>
          ))}
        </select>
      </div>

      <div className="mb-8">
        <h2 className="text-2xl font-bold">時限</h2>
        <select
          className="mt-4 w-full rounded-lg border-2 p-2"
          value={period}
          onChange={handlePeriodChange}
        >
          <option value="">時限を選択</option>
          {['1', '2', '3', '4', '5', '6'].map((period) => (
            <option key={period} value={period}>
              {period}限
            </option>
          ))}
        </select>
      </div>

      <button
        className="mt-4 w-full rounded-lg bg-blue-500 px-4 py-2 text-white"
        onClick={searchClasses}
      >
        検索
      </button>
    </div>
  );
}
