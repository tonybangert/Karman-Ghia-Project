import { useEffect, useRef, type ReactNode } from 'react'
import { AnimatePresence, motion, useReducedMotion } from 'framer-motion'
import { cx } from '@/lib/cx'

interface Props {
  open: boolean
  onClose: () => void
  label: string
  children: ReactNode
  side?: boolean // slide-in drawer vs centered dialog
}

export function Modal({ open, onClose, label, children, side = false }: Props) {
  const ref = useRef<HTMLDivElement>(null)
  const reduce = useReducedMotion()

  useEffect(() => {
    if (!open) return
    const onKey = (e: KeyboardEvent) => e.key === 'Escape' && onClose()
    document.addEventListener('keydown', onKey)
    const prev = document.body.style.overflow
    document.body.style.overflow = 'hidden'
    ref.current?.focus()
    return () => {
      document.removeEventListener('keydown', onKey)
      document.body.style.overflow = prev
    }
  }, [open, onClose])

  return (
    <AnimatePresence>
      {open && (
        <motion.div
          className="fixed inset-0 z-50 flex"
          initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
          transition={{ duration: reduce ? 0 : 0.2 }}
        >
          <div className="absolute inset-0 bg-black/70 backdrop-blur-[2px]" onClick={onClose} aria-hidden />
          <motion.div
            ref={ref}
            role="dialog" aria-modal="true" aria-label={label} tabIndex={-1}
            className={cx(
              'relative z-10 m-auto max-h-[90vh] w-full overflow-y-auto outline-none',
              side
                ? 'ml-auto h-full max-w-xl border-l border-line bg-surface-elevated shadow-panel'
                : 'max-w-2xl rounded-xl border border-line bg-surface-elevated shadow-panel'
            )}
            initial={reduce ? { opacity: 0 } : side ? { x: 40, opacity: 0 } : { y: 20, opacity: 0 }}
            animate={{ x: 0, y: 0, opacity: 1 }}
            exit={reduce ? { opacity: 0 } : side ? { x: 40, opacity: 0 } : { y: 20, opacity: 0 }}
            transition={{ type: 'spring', stiffness: 320, damping: 32 }}
          >
            <button
              onClick={onClose}
              className="absolute right-3 top-3 z-20 grid h-8 w-8 place-items-center rounded-md border border-line bg-surface text-ink-muted hover:text-ink"
              aria-label="Close"
            >✕</button>
            {children}
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  )
}
