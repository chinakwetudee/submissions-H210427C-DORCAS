<script>
	import { Separator } from "$lib/components/ui/separator/index.js";
	import { cn } from "$lib/components/shadcn/utils.js";
	let { ref = $bindable(null), class: className, ...restProps } = $props();
</script>

<Separator
	bind:ref
	data-sidebar="separator"
	class={cn("bg-sidebar-border mx-2 w-auto", className)}
	{...restProps}
/>
