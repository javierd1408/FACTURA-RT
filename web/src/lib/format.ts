export function formatMoney(value: number, decimals: number = 2) {
return value.toLocaleString('es-VE', { minimumFractionDigits: decimals, maximumFractionDigits: decimals })
}