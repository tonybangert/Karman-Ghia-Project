import { clsx, type ClassValue } from 'clsx'
import { twMerge } from 'tailwind-merge'
export const cx = (...a: ClassValue[]) => twMerge(clsx(a))
