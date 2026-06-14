"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { sidebarItems } from "./sidebar-items";

export function Sidebar() {
  const pathname = usePathname();

  return (
    <aside className="hidden md:flex md:w-72 flex-col border-r border-[var(--border)] bg-white">
      <div className="h-16 px-6 flex items-center border-b border-[var(--border)]">
        <div>
          <h1 className="text-lg font-bold text-[var(--primary)]">
            Amicale SL
          </h1>

          <p className="text-xs text-slate-500">
            Université Alioune Diop
          </p>
        </div>
      </div>

      <nav className="flex-1 p-4 space-y-2">
        {sidebarItems.map((item) => {
          const Icon = item.icon;

          const isActive =
            pathname === item.href ||
            pathname.startsWith(`${item.href}/`);

          return (
            <Link
              key={item.href}
              href={item.href}
              className={`flex items-center gap-3 rounded-xl px-4 py-3 transition-all
              ${
                isActive
                  ? "bg-gradient-to-r from-[var(--primary)] to-blue-700 text-white shadow-md font-medium"
                  : "text-slate-600 hover:bg-slate-100 hover:text-[var(--primary)]"
              }`}
            >
              <Icon size={22} weight="duotone" />

              <span>{item.title}</span>
            </Link>
          );
        })}
      </nav>
    </aside>
  );
}
