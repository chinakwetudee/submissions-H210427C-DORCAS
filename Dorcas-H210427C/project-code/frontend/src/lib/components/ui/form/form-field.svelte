<script>
	import * as FormPrimitive from "formsnap";
	import { cn } from "$lib/components/shadcn/utils.js";
	let {
		ref = $bindable(null),
		class: className,
		form,
		name,
		children: childrenProp,
		...restProps
	} = $props();
</script>

<FormPrimitive.Field {form} {name}>
	{#snippet children({ constraints, errors, tainted, value })}
		<div bind:this={ref} class={cn("space-y-2", className)} {...restProps}>
			{@render childrenProp?.({ constraints, errors, tainted, value: value })}
		</div>
	{/snippet}
</FormPrimitive.Field>
