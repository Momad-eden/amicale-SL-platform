import { DashboardStats } from "@/types/dashboard";

export async function getDashboardStats(): Promise<DashboardStats> {
  const response = await fetch(
    "http://127.0.0.1:8000/api/dashboard/stats/",
    {
      cache: "no-store",
    }
  );

  if (!response.ok) {
    throw new Error("Impossible de récupérer les statistiques.");
  }

  return response.json();
}