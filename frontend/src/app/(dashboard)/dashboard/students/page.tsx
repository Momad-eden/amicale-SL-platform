import { getStudents } from "@/services/students";
import { StudentsTable } from "@/components/students/students-table";

export default async function StudentsPage() {
  const students = await getStudents();

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold">
            Étudiants
          </h1>

          <p className="text-slate-500">
            Gestion des membres de l'amicale.
          </p>
        </div>

        <button className="rounded-xl bg-[var(--primary)] px-5 py-3 text-white font-medium hover:opacity-90">
          Ajouter un étudiant
        </button>
      </div>

      <StudentsTable students={students} />
    </div>
  );
}