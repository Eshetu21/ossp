"use client";
import { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCheckCircle } from "@fortawesome/free-solid-svg-icons";

export default function HateSpeechDetector() {
  const [text, setText] = useState("");
  const [result, setResult] = useState("");

  const analyzeText = async () => {
    const response = await fetch("http://localhost:8000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ comment_text: text }),
    });

    if (response.ok) {
      const data = await response.json();
      setResult(data.result);
    } else {
      setResult("Error: Unable to process the request.");
    }
  };

  return (
    <div className="flex flex-col lg:flex-row lg:mt-10 items-center justify-around p-6 lg:p-12 ">
      <div className=" max-w-lg text-center lg:text-left">
        <h1 className="text-3xl lg:text-5xl font-bold text-gray-700 mb-4">
          Hate Speech Detector
        </h1>
        <p className="text-lg text-gray-600 mb-2">
          Detecting hate speech has always been{" "}
          <span className="text-red-600 font-semibold">SLOW</span> and{" "}
          <span className="text-red-600 font-semibold">EXPENSIVE</span>.
        </p>
        <p className="text-lg text-gray-600 mb-6">
          Not anymore! Introducing a fast, free, and open-source hate speech
          detection web app.
        </p>
        <ul className="space-y-4">
          <li className="flex items-center">
            <FontAwesomeIcon
              icon={faCheckCircle}
              className="text-green-500 mr-2"
            />
            <span className="text-gray-600">Faster and cheaper than AI</span>
          </li>
          <li className="flex items-center">
            <FontAwesomeIcon
              icon={faCheckCircle}
              className="text-green-500 mr-2"
            />
            <span className="text-gray-600">Pretty accurate</span>
          </li>
          <li className="flex items-center">
            <FontAwesomeIcon
              icon={faCheckCircle}
              className="text-green-500 mr-2"
            />
            <span className="text-gray-600">100% free & open-source</span>
          </li>
        </ul>
      </div>

      <div className="mt-8 lg:mt-0 lg:ml-12 w-full max-w-lg">
        <textarea
          className="w-full h-50 p-4 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-400"
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter text to analyze"
        ></textarea>
        <button
          onClick={analyzeText}
          className="mt-4 w-full py-2 bg-green-500 text-white font-semibold rounded-lg hover:bg-green-600 transition"
        >
          Analyze
        </button>
        <p className="mt-4 text-lg text-gray-700">
          <span className="font-semibold">Result:</span> {result}
        </p>
      </div>
    </div>
  );
}

