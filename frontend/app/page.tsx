"use client";

import { useState } from 'react';

export default function Home() {
    const [message, setMessage] = useState('');
    const [response, setResponse] = useState<string | null>(null);
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setResponse(null);

        const res = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message }),
        });

        const data = await res.json();
        setResponse(data.response);
        setLoading(false);
    };

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Chatbot</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                    placeholder="输入你的消息"
                    className="w-full p-2 border rounded"
                />
                <button
                    type="submit"
                    className="mt-4 bg-blue-500 text-white py-2 px-4 rounded"
                >
                    发送
                </button>
            </form>
            {loading && <p className="mt-4">正在生成回复...</p>}
            {response && (
                <div className="mt-6">
                    <h2 className="text-xl font-semibold">回复：</h2>
                    <p className="mt-2">{response}</p>
                </div>
            )}
        </div>
    );
}
