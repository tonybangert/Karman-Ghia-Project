import { createContext, useContext, type ReactNode } from 'react'
import { archive, type Archive } from './archive'

const ArchiveContext = createContext<Archive>(archive)

export function ArchiveProvider({ children }: { children: ReactNode }) {
  return <ArchiveContext.Provider value={archive}>{children}</ArchiveContext.Provider>
}

export const useArchive = () => useContext(ArchiveContext)
