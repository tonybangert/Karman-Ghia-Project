import { useDocViewer } from './DocViewer'
import { cx } from '@/lib/cx'

export function DocChip({ id, className }: { id: string; className?: string }) {
  const open = useDocViewer()
  return (
    <button className={cx('doc-chip', className)} onClick={() => open(id)} title="View source document">
      {id}
    </button>
  )
}
