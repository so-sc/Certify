"use client";

import { useState } from "react";
// import dotenv from "dotenv";
// dotenv.config();
require('dotenv').config();

const base_url = process.env.BASE_URL;

export default function Home() {
  const [certificate, setCertificate] = useState(null);

    async function copyCertificate() {
        if (!certificate) {
            alert("No link to copy");
            return;
        }
        navigator.clipboard.writeText(certificate)
        .then(() => {
            alert('Copied to clipboard!');
        })
        .catch((err) => {
            console.error('Failed to copy: ', err);
        });
    }

  async function uploadCertificate(e: any) {
    if (!e.target.files[0]) {
      alert("Please upload a file");
      return;
    }
    const formData = new FormData();
    formData.append("file", e.target.files[0], e.target.files[0].name);
    const res = await fetch(`http://localhost:8000/api/v1/template`, {
        method: 'POST',
        body: formData,
    });
    const data = await res.json();
    if (!data.success) {
        alert(data.message);
    } else {
        setCertificate(data.dl);
    }
  }

  return (
      <div className="h-full">
          <div className="flex items-center justify-between">
              <div className="container pt-4 md:pt-8 mx-auto m-4 flex flex-wrap flex-col md:flex-row items-center">
                  <div className="flex flex-col w-full justify-center overflow-y-hidden">
                        <h1 className="mb-3 text-3xl md:text-5xl text-white opacity-75 font-bold leading-tight text-center">
                          Welcome To
                          <a href="/" className="pl-3 bg-clip-text text-transparent bg-gradient-to-r from-green-400 via-pink-500 to-purple-500 hover:text-transparent hover:no-underline hover:no-underline">
                            Certify
                          </a>, Explore Effectively!
                        </h1>
                      {certificate ?(
                        <div className="flex items-end justify-center w-full pt-20 px-20">
                            <div className="relative w-3/5 mr-4 text-left md:w-full lg:w-full xl:w-1/2">
                                <div className="relative">
                                    <input className="w-full px-4 py-3 text-xl font-medium leading-8 text-white transition duration-200 ease-in-out bg-gray-700 border-transparent rounded-md shadow-2xl outline-none border-y border-t-gray-600 focus:border focus:border-blue-600 focus:bg-transparent focus:ring-2 focus:ring-blue-600" readOnly={true} value={certificate} />
                                    <a href={certificate} target="_blank" rel="noreferrer">
                                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" className="absolute w-6 h-6 text-orange-600 transform -translate-y-1/2 right-3 top-1/2">
                                            <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 6H5.25A2.25 2.25 0 003 8.25v10.5A2.25 2.25 0 005.25 21h10.5A2.25 2.25 0 0018 18.75V10.5m-10.5 6L21 3m0 0h-5.25M21 3v5.25"></path>
                                        </svg>
                                    </a>
                                </div>
                            </div>
                            <button onClick={copyCertificate} type="button" className="inline-flex flex-shrink-0 px-6 py-3 text-lg font-semibold text-white transition bg-orange-600 border-0 rounded hover:bg-orange-600 hover:brightness-50 focus:outline-none">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" className="w-6 h-6 transition"><path stroke-linecap="round" stroke-linejoin="round" d="M15.75 17.25v3.375c0 .621-.504 1.125-1.125 1.125h-9.75a1.125 1.125 0 01-1.125-1.125V7.875c0-.621.504-1.125 1.125-1.125H6.75a9.06 9.06 0 011.5.124m7.5 10.376h3.375c.621 0 1.125-.504 1.125-1.125V11.25c0-4.46-3.243-8.161-7.5-8.876a9.06 9.06 0 00-1.5-.124H9.375c-.621 0-1.125.504-1.125 1.125v3.5m7.5 10.375H9.375a1.125 1.125 0 01-1.125-1.125v-9.25m12 6.625v-1.875a3.375 3.375 0 00-3.375-3.375h-1.5a1.125 1.125 0 01-1.125-1.125v-1.5a3.375 3.375 0 00-3.375-3.375H9.75"></path></svg>
                                <span id="copyBtn">COPY</span>
                            </button>
                        </div>
                      ):(
                        <>
                        <p className="leading-normal text-base md:text-2xl mb-8 text-center">
                            Upload your certificate template!
                        </p>
                        <div className="relative text-left w-full">
                            <div className="relative flex items-center justify-center px-4 pt-12 pb-8 bg-no-repeat bg-cover sm:px-6 lg:px-8">
                                <div className="z-10 w-full p-5 bg-gray-700 bg-opacity-70 sm:max-w-lg rounded-xl">
                                    <div className="text-center">
                                        <h2 className="mt-2 text-3xl font-bold text-gray-200">Certificate Template Upload!</h2>
                                        <p className="mt-2 text-sm text-gray-200">Store the template.</p>
                                    </div>
                                    <form className="space-y-3">
                                    <div className="grid grid-cols-1 space-y-2">
                                        <label className="text-sm font-bold tracking-wide text-gray-200">Attach .PPTX</label>
                                        <div className="flex items-center justify-center w-full">
                                            <label className="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-200 border-dashed rounded-lg cursor-pointer hover:bg-white hover:bg-opacity-20">
                                                <div className="flex flex-col items-center justify-center pt-5 pb-6">
                                                    <div className="flex flex-auto">
                                                        <img className="object-center h-36" src="/assets/upload.svg" alt="upload" />
                                                    </div>
                                                    <p className="text-center text-gray-200 pointer-none p-2">
                                                        <span className="text-sm">Drag and drop</span> pptx file here <br /> or <span className="font-bold text-orange-600">Click to upload</span> from your computer
                                                    </p>
                                                </div>
                                                <input id="file" name="file" type="file" className="hidden" accept=".pptx" required={true} onChange={uploadCertificate} />
                                            </label>
                                            </div>
                                            <p className="text-sm text-gray-200 pointer-none">
                                                <span>File type: pptx only.</span>
                                            </p>
                                        </div>
                                    </form>
                                </div>
                            </div>
                        </div>
                        </>
                      )}
                  </div>
              </div>
          </div>
          {/* <!--<div className="flex space-x-2 justify-end">
              <div>
                  <button type="button" className="inline-block rounded-full bg-blue-500 hover:bg-blue-700 border-blue-600 hover:border-blue-800 leading-normal uppercase text-white bg-color shadow-md hover:shadow-lg focus:shadow-lg focus:outline-none focus:ring-0 active:shadow-lg transform hover:scale-125 duration-300 ease-in-out transition w-9 h-9">
                      <img alt="Telegram" src="https://www.svgrepo.com/show/299513/telegram.svg">
                  </button>
              </div>
          </div>--> */}
      </div>
  );
}
