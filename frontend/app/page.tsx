"use client";

import { useState } from 'react';
import axios from 'axios';

export default function Home() {
    const [message, setMessage] = useState('');
    const [response, setResponse] = useState<string | null>(null);
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setResponse(null);
        try
        {
            const res = await axios.post('/api/chat', 
                { 
                    message 
                }, 
                {
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    timeout: 100000  // 超时时间设置为 60 秒
                });
        }
        catch (error)
        {
            console.error(error);
            setResponse("Error: 生成文章失败，请稍后重试。" + error);
        }

        setLoading(false);
    };

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">EssayWriter</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                    placeholder="输入你的文章主题..."
                    className="w-full p-2 border rounded"
                />
                <button
                    type="submit"
                    className="mt-4 bg-blue-500 text-white py-2 px-4 rounded"
                    disabled={loading}
                >
                {loading ? '正在生成...' : '生成文章'}
                </button>
            </form>
            {loading && <p className="mt-4">正在生成文章，请稍候...</p>}
            {response && !loading && (
                <div className="mt-6">
                    <h2 className="text-xl font-semibold">生成的文章:</h2>
                    <p className="mt-2">{response}</p>
                </div>
            )}
        </div>
    );
}
