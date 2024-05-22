'use client';
import React, { useState } from 'react';

interface ClassData {
  id: number;
  name: string;
  credits: number;
  semester: string;
  teacher: string;
  department: string;
  day: string;
  period: string;
  plan: string;
  how_grading: string;
  caution: string;
}

export default function Search() {
  const [department, setDepartment] = useState('');
  const [day, setDay] = useState('');
  const [period, setPeriod] = useState('');
  const [classes, setClasses] = useState<ClassData[]>([]);
  const [searched, setSearched] = useState(false);

  const handleDepartmentChange = (event: { target: { value: React.SetStateAction<string> } }) => {
    setDepartment(event.target.value);
  };

  const handleDayChange = (event: { target: { value: React.SetStateAction<string> } }) => {
    setDay(event.target.value);
  };

  const handlePeriodChange = (event: { target: { value: React.SetStateAction<string> } }) => {
    setPeriod(event.target.value);
  };

  const searchClasses = async () => {
    setSearched(true);
    const queryParams = new URLSearchParams({
      department,
      day,
      period,
    }).toString();

    const url = `http://127.0.0.1:8080/search?${queryParams}`;

    const response = await fetch(url, {
      headers: {
        Accept: 'application/json',
      },
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    setClasses(data);
    console.log(data);
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
          <option value="マテリアル工学科">マテリアル工学科</option>
          <option value="建築学科">建築学科</option>
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
      <div className="mt-8 space-y-4">
        {searched ? (
          classes.length > 0 ? (
            classes.map((cls: ClassData) => (
              <div key={cls.id} className="rounded-lg bg-white p-4 shadow-lg">
                <h3 className="text-xl font-bold">{cls.name}</h3>
                <p className="text-gray-800">学科: {cls.department}</p>
                <p className="text-gray-800">クレジット: {cls.credits}</p>
                <p className="text-gray-800">セメスター: {cls.semester}</p>
                <p className="text-gray-800">教師: {cls.teacher}</p>
                <p className="text-gray-800">曜日: {cls.day}</p>
                <p className="text-gray-800">時限: {cls.period}</p>
                <p className="text-gray-800">計画: {cls.plan}</p>
                <p className="text-gray-800">評価方法: {cls.how_grading}</p>
                <p className="text-gray-800">注意: {cls.caution}</p>
              </div>
            ))
          ) : (
            <p className="text-center text-xl text-gray-800">
              該当する授業は見つかりませんでした。
            </p>
          )
        ) : null}
      </div>
    </div>
  );
}
