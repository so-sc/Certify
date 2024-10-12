import type { Metadata } from "next";
import "./globals.css";

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
      <body
        className="antialiased">
        {children}
      </body>
    </html>
  );
}
