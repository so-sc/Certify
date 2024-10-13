import type { Metadata } from "next";
import  "bootstrap/dist/css/bootstrap.min.css"
import "./globals.css";
import Footer from "@/component/footer";
import Headers from "@/component/header";

export const metadata: Metadata = {
  title: "Certify",
  description: "This is an application as a service to generate and store certificate for SOSC Events",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="leading-normal tracking-normal text-indigo-400 m-6 bg-cover bg-fixed" style={{backgroundImage: `url('https://picdb.vercel.app/assets/home.jpg')`}}>
        <Headers />
        {children}
        <Footer />
        {/* <script src="https://cdn.jsdelivr.net/npm/jquery@3.4.1/dist/jquery.slim.min.js" integrity="sha256-pasqAKBDmFT4eHoN2ndd6lN370kFiGUFyTiUHWhU7k8=" crossOrigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossOrigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/js/bootstrap.min.js" integrity="sha256-WqU1JavFxSAMcLP2WIOI+GB2zWmShMI82mTpLDcqFUg=" crossOrigin="anonymous"></script> */}
      </body>
    </html>
  );
}
