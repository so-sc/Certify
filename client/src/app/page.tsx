"use client";

import { useState } from "react";

export default function Home() {
  const [template, setTemplate] = useState("");
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [id, setId] = useState("");
  const [body, setBody] = useState("");
  const [subject, setSubject] = useState("");
  const [certificate, setCertificate] = useState("");

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

  async function generate_certificate(e: any) {
    if (template === "" || name === "" || id === "") {
      alert("Please fill all the required fields");
      return;
    }
    var url;
    const formData = new FormData();
    if (template && name && id) {
      url = `http://localhost:8000/api/v1/generate-url?url=${template}&name=${name}&user_id=${id}`
    } else if (template && name && id && email && body && subject) {
      url = `http://localhost:8000/api/v1/generate-url-email?url=${template}&name=${name}&user_id=${id}&email=${email}&body=${body}&subject=${subject}`
    } else {
      return alert("Please fill all the required fields");
    }
    const res = await fetch(url, {
      method: 'POST'
    });
    console.log("Fetched response");
    const data = await res.json();
    console.log(data);
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
                  <div className="flex flex-col w-full justify-center overflow-y-hidden px-[150px]">
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
                          This is free service to generating certificate!
                      </p>
                      <form action={generate_certificate} className="bg-gray-900 opacity-95 w-full shadow-lg rounded-lg px-8 pt-6 pb-8 mb-4">
                          <div className="m-5 mb-0">
                            <label className="block text-blue-300 py-2 font-bold mb-2" htmlFor="email">
                              Certificate URL<span className="text-red-600"> *</span>
                            </label>
                            <input required={true} onChange={(e) => setTemplate(e.target.value)} className="shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out form-control" type="text" placeholder="https://example.com/" />
                          </div>
                          <div className="mb-0 m-5 mt-0 flex space-x-4">
                              <div className="w-1/2">
                                <label className="block text-blue-300 py-2 font-bold mb-2" htmlFor="name">
                                Name<span className="text-red-600"> *</span>
                                </label>
                                <input required={true} onChange={(e) => setName(e.target.value)} className="shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out form-control" type="text" placeholder="Akkil M G" />
                              </div>
                              <div className="w-1/2">
                                <label className="block text-blue-300 py-2 font-bold mb-2" htmlFor="id">
                                Id<span className="text-red-600"> *</span>
                                </label>
                                <input required={true} onChange={(e) => setId(e.target.value)} className="shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out form-control" type="text" placeholder="asdewbc3hjb2h" />
                              </div>
                          </div>
                          <div className="m-5 mt-0 mb-0">
                            <label className="block text-blue-300 py-2 font-bold mb-2" htmlFor="email">
                              Email
                            </label>
                            <input onChange={(e) => setEmail(e.target.value)} className="shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out form-control" type="text" placeholder="email@name.domain" />
                          </div>
                          <div className="mb-4 m-5 mt-0 flex space-x-4">
                              <div className="w-1/2">
                                <label className="block text-blue-300 py-2 font-bold mb-2" htmlFor="name">
                                Subject
                                </label>
                                <textarea onChange={(e) => setSubject(e.target.value)} className="shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out form-control" placeholder="Congratulating on participating in the event"></textarea>
                              </div>
                              <div className="w-1/2">
                                <label className="block text-blue-300 py-2 font-bold mb-2" htmlFor="id">
                                Body
                                </label>
                                <textarea onChange={(e) => setBody(e.target.value)} className="shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out form-control" placeholder="We are thrilled to congratulate you..."></textarea>
                              </div>
                          </div>
                          <div className=" flex items-center justify-between pt-4">
                              <div className="px-5 input-group-append">
                                  <button className="bg-gradient-to-r from-purple-800 to-green-500 hover:from-pink-500 hover:to-green-500 text-white font-bold py-2 px-10 rounded focus:ring transform transition hover:scale-105 duration-300 ease-in-out btn btn-primary" type="submit" id="searchbtn">
                                  Generate
                                  </button>
                              </div>
                          </div>
                      </form>
                      {/* <div className="modal fade" id="exampleModal" tabIndex={-1} role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                          <div className="modal-dialog" role="document">
                            <div className="modal-content">
                                <div className="modal-header">
                                  <h5 className="modal-title" id="exampleModalLabel">Result</h5>
                                  <button type="button" className="close" data-dismiss="modal" aria-label="Close">
                                      <span aria-hidden="true">×</span>
                                  </button>
                                </div>
                                <div className="modal-body" id="result">No result</div>
                                <div className="modal-footer">
                                  <button type="button" className="btn btn-primary" onClick={(e) => {}} data-toggle="popover" data-placement="bottom" data-content="Copied!" data-original-title="" title="">Copy</button>
                                  <button type="button" className="btn btn-secondary" data-dismiss="modal">Close</button>    
                                </div>
                            </div>
                          </div>
                      </div>  */}
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
