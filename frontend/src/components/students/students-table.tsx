import { Student } from "@/types/student";

export function StudentsTable({
  students,
}: {
  students: Student[];
}) {
  return (
    <div className="overflow-hidden rounded-2xl border border-[var(--border)] bg-white shadow-sm">
      <table className="w-full">
        <thead className="bg-slate-50">
          <tr className="text-left text-sm text-slate-600">
            <th className="px-6 py-4">Étudiant</th>
            <th className="px-6 py-4">Niveau</th>
            <th className="px-6 py-4">Téléphone</th>
            <th className="px-6 py-4">Résident</th>
            <th className="px-6 py-4">Statut</th>
          </tr>
        </thead>

        <tbody>
          {students.map((student) => (
            <tr
              key={student.id}
              className="border-t border-[var(--border)]"
            >
              <td className="px-6 py-4">
                <div className="flex items-center gap-3">
                  {student.photo_url ? (
                    <img
                      src={student.photo_url}
                      alt={student.full_name}
                      className="h-10 w-10 rounded-full object-cover"
                    />
                  ) : (
                    <div className="h-10 w-10 rounded-full bg-[var(--primary)] text-white flex items-center justify-center font-semibold">
                      {student.full_name.charAt(0)}
                    </div>
                  )}

                  <span className="font-medium text-slate-900">
                    {student.full_name}
                  </span>
                </div>
              </td>

              <td className="px-6 py-4">
                {student.level_display}
              </td>

              <td className="px-6 py-4">
                {student.phone}
              </td>

              <td className="px-6 py-4">
                {student.is_resident ? (
                  <span className="rounded-full bg-blue-50 px-3 py-1 text-xs font-medium text-blue-700 border border-blue-200">
                    Résident
                  </span>
                ) : (
                  <span className="rounded-full bg-amber-50 px-3 py-1 text-xs font-medium text-amber-700 border border-amber-200">
                    Non résident
                  </span>
                )}
              </td>

              <td className="px-6 py-4">
                <span className="rounded-full bg-green-100 px-3 py-1 text-xs font-medium text-green-800">
                  {student.academic_status_display}
                </span>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}