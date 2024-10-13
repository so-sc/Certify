"use client";

export default function Header() {
    return (
        <header className="flex flex-col md:justify-center sticky -top-[1px] z-50 bg-[#0B0B0B] bg-opacity-80 backdrop-blur-xl min-h-max">
            <nav className="flex justify-between px-6 md:px-8 pb-3 md:py-5">
                <a className="flex text-white align-top" href="/">
                    <img alt="Certify" fetchPriority="high" width="107" height="30" sizes="(max-width: 640px) 85px, 107px" src="/assets/logo.png" style={{color: 'transparent'}} />
                </a>
                <a href="/certificate" className="transform transition hover:scale-105 duration-300 ease-in-out flex items-center">
                    <button className="font-semibold text-sm px-2 py-2 rounded-lg max-h-[32px] bg-white hover:bg-gray-300 transition-all text-black w-full font-medium font-fredoka tracking-wide flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed md:max-w-[205px]" type="button">Certificate</button>
                </a>
            </nav>
        </header>
    );
}