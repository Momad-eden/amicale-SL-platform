"use client";

import {
  Bell,
  MagnifyingGlass,
} from "@phosphor-icons/react";

export function Header() {
  const today = new Intl.DateTimeFormat("fr-FR", {
    weekday: "long",
    day: "numeric",
    month: "long",
    year: "numeric",
  }).format(new Date());

  return (
    <header className="sticky top-0 z-20 flex h-20 items-center justify-between border-b border-[var(--border)] bg-white/95 px-6 backdrop-blur-sm">
      {/* Partie gauche */}
      <div className="flex flex-col">
        <p className="text-sm text-slate-500">
          Bonjour 👋
        </p>

        <h2 className="text-xl font-bold text-slate-900">
          Momar Diop
        </h2>

        <p className="text-xs capitalize text-slate-500">
          {today}
        </p>
      </div>

      {/* Recherche */}
      <div className="mx-8 hidden flex-1 lg:flex lg:justify-center">
        <div className="relative w-full max-w-lg">
          <MagnifyingGlass
            size={20}
            weight="duotone"
            className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400"
          />

          <input
            type="text"
            placeholder="Rechercher un étudiant, une maison..."
            className="
              w-full rounded-2xl border border-[var(--border)]
              bg-slate-50 py-3 pl-12 pr-4 text-sm
              outline-none transition
              placeholder:text-slate-400
              focus:border-[var(--primary)]
              focus:bg-white
              focus:ring-4 focus:ring-blue-100
            "
          />
        </div>
      </div>

      {/* Partie droite */}
      <div className="flex items-center gap-4">
        {/* Notifications */}
        <button
          className="
            relative rounded-2xl border border-[var(--border)]
            bg-white p-3 transition
            hover:border-[var(--primary)]
            hover:bg-slate-50
          "
        >
          <Bell
            size={22}
            weight="duotone"
            className="text-slate-700"
          />

          <span
            className="
              absolute -right-1 -top-1
              flex h-5 w-5 items-center justify-center
              rounded-full bg-[var(--secondary)]
              text-[10px] font-bold text-slate-900
            "
          >
            2
          </span>
        </button>

        {/* Profil */}
        <button
          className="
            flex items-center gap-3 rounded-2xl
            border border-[var(--border)]
            bg-white px-3 py-2 transition
            hover:border-[var(--primary)]
            hover:bg-slate-50
          "
        >
          <div
            className="
              flex h-11 w-11 items-center justify-center
              rounded-2xl bg-gradient-to-br
              from-[var(--primary)]
              to-blue-700
              font-bold text-white shadow-md
            "
          >
            MD
          </div>

          <div className="hidden text-left md:block">
            <p className="text-sm font-semibold text-slate-900">
              Momar Diop
            </p>

            <p className="text-xs text-slate-500">
              Administrateur
            </p>
          </div>
        </button>
      </div>
    </header>
  );
}