export interface Student {
  id: number;

  full_name: string;

  photo_url: string | null;

  level: string;
  level_display: string;

  phone: string;

  is_resident: boolean;

  academic_status: string;
  academic_status_display: string;
}