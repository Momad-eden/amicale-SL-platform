import { getDashboardStats } from "@/services/dashboard";

export default async function DashboardPage() {
  const stats = await getDashboardStats();

  return (
    <div className="space-y-6">
      <div className="rounded-3xl overflow-hidden bg-gradient-to-r from-[var(--primary)] to-blue-700 text-white p-8 shadow-lg">
        <p className="text-sm uppercase tracking-widest text-blue-100">
          Amicale des Étudiants de Saint-Louis à Bambey
        </p>

        <h1 className="mt-3 text-3xl font-bold">
          Solidarité • Excellence • Engagement
        </h1>

        <p className="mt-3 text-blue-100 max-w-2xl">
          Une plateforme moderne pour accompagner, organiser et renforcer la vie étudiante.
        </p>
      </div>

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
        <StatCard
          title="Étudiants"
          value={stats.students.toString()}
          accent="blue"
        />

        <StatCard
          title="Maisons"
          value={stats.houses.toString()}
          accent="yellow"
        />

        <StatCard
          title="Occupations"
          value={stats.occupied.toString()}
          accent="green"
        />

        <StatCard
          title="Disponibles"
          value={stats.available.toString()}
          accent="indigo"
        />
      </div>

      <div className="rounded-2xl bg-white p-6 shadow-sm border border-[var(--border)]">
        <h2 className="text-lg font-semibold">
          Alertes importantes
        </h2>

        <div className="mt-4 space-y-3 text-sm">
          <div className="rounded-xl bg-yellow-50 p-4 text-yellow-800">
            ⚠️ Aucune affectation active actuellement.
          </div>

          <div className="rounded-xl bg-blue-50 p-4 text-blue-800">
            👨‍🎓 {stats.students} étudiant(s) enregistré(s).
          </div>
        </div>
      </div>
    </div>
  );
}

function StatCard({
  title,
  value,
  accent,
}: {
  title: string;
  value: string;
  accent: "blue" | "yellow" | "green" | "indigo";
}) {
  const accents = {
    blue: "border-l-4 border-blue-600",
    yellow: "border-l-4 border-yellow-500",
    green: "border-l-4 border-green-600",
    indigo: "border-l-4 border-indigo-600",
  };

  return (
    <div
      className={`rounded-2xl bg-white p-6 shadow-sm hover:shadow-md transition ${accents[accent]}`}
    >
      <p className="text-sm text-slate-500">
        {title}
      </p>

      <p className="mt-3 text-4xl font-bold text-slate-900">
        {value}
      </p>
    </div>
  );
}