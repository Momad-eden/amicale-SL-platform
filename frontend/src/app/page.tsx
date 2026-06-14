"use client";

import { useEffect, useState } from "react";
import { api } from "@/services/api";

export default function Home() {
  const [message, setMessage] = useState("Chargement...");

  useEffect(() => {
    api.get("/health/")
      .then((response) => {
        setMessage(response.data.message);
      })
      .catch(() => {
        setMessage("Impossible de joindre le backend.");
      });
  }, []);

  return (
    <main className="min-h-screen flex flex-col items-center justify-center px-6">
      <h1 className="text-4xl font-bold text-center">
        Amicale des Étudiants de Saint-Louis à Bambey
      </h1>

      <p className="mt-6 text-lg">
        {message}
      </p>
    </main>
  );
}