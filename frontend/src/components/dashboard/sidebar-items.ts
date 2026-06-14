import {
  Gauge,
  UsersThree,
  House,
  CurrencyCircleDollar,
  CalendarDots,
  Newspaper,
  Images,
  ChartBar,
  Gear,
} from "@phosphor-icons/react";

export const sidebarItems = [
  {
    title: "Dashboard",
    href: "/dashboard",
    icon: Gauge,
  },
  {
    title: "Étudiants",
    href: "/dashboard/students",
    icon: UsersThree,
  },
  {
    title: "Logements",
    href: "/dashboard/houses",
    icon: House,
  },
  {
    title: "Cotisations",
    href: "/dashboard/payments",
    icon: CurrencyCircleDollar,
  },
  {
    title: "Événements",
    href: "/dashboard/events",
    icon: CalendarDots,
  },
  {
    title: "Actualités",
    href: "/dashboard/news",
    icon: Newspaper,
  },
  {
    title: "Galerie",
    href: "/dashboard/gallery",
    icon: Images,
  },
  {
    title: "Rapports",
    href: "/dashboard/reports",
    icon: ChartBar,
  },
  {
    title: "Paramètres",
    href: "/dashboard/settings",
    icon: Gear,
  },
];