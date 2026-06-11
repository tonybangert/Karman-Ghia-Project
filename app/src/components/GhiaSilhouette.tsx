import type { ReactNode } from 'react'
import { cx } from '@/lib/cx'

// Stylized Type 14 Ghia side profile, nose to the right. viewBox 1000 x 360.
// Hotspot overlays in the explorer are positioned against this same viewBox.
export const GHIA_VIEWBOX = '0 0 1000 360'
const BODY =
  'M70,256 L172,256 Q250,150 328,256 L690,256 Q762,150 838,256 L905,256 ' +
  'Q968,250 958,205 Q950,150 858,150 L612,150 Q590,150 560,124 L470,86 ' +
  'Q380,52 300,86 L150,150 Q70,165 62,210 Z'

export function GhiaSilhouette({
  className, bodyClassName, children, decorative = false,
}: {
  className?: string
  bodyClassName?: string
  children?: ReactNode
  decorative?: boolean
}) {
  return (
    <svg viewBox={GHIA_VIEWBOX} className={className} role="img" aria-label="Side profile of a 1965 VW Karmann Ghia coupe" preserveAspectRatio="xMidYMid meet">
      {/* belt / character line */}
      <path d={BODY} className={cx('fill-current', bodyClassName)} />
      <path d="M150,150 L612,150" className="stroke-current opacity-30" strokeWidth={2} fill="none" />
      {/* greenhouse glass */}
      <path d="M300,92 L462,92 L556,126 L312,126 Z" className="fill-black/40" />
      {/* wheels */}
      {[250, 762].map((cx0) => (
        <g key={cx0}>
          <circle cx={cx0} cy={252} r={62} className="fill-black/55" />
          <circle cx={cx0} cy={252} r={62} className="stroke-current opacity-40" strokeWidth={3} fill="none" />
          <circle cx={cx0} cy={252} r={26} className="stroke-current opacity-30" strokeWidth={3} fill="none" />
        </g>
      ))}
      {/* headlight + nostril hints */}
      {!decorative && <circle cx={915} cy={170} r={11} className="fill-black/30" />}
      {children}
    </svg>
  )
}
