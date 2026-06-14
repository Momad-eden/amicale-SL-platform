import { Student } from "@/types/student";

export async function getStudents(): Promise<Student[]> {
  const response = await fetch(
    "http://127.0.0.1:8000/api/students/",
    {
      cache: "no-store",
    }
  );

  if (!response.ok) {
    throw new Error(
      "Impossible de récupérer les étudiants."
    );
  }

  return response.json();
}