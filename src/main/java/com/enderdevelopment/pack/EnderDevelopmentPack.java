package com.enderdevelopment.pack;

import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.common.event.FMLPreInitializationEvent;
import org.apache.logging.log4j.Logger;

@Mod(modid = EnderDevelopmentPack.MOD_ID, name = EnderDevelopmentPack.NAME, version = EnderDevelopmentPack.VERSION)
public final class EnderDevelopmentPack {
    public static final String MOD_ID = "enderdevelopmentpack";
    public static final String NAME = "EnderDevelopment 1.12.2 Pack";
    public static final String VERSION = "1.0.0";

    private static Logger logger;

    @Mod.EventHandler
    public void preInit(FMLPreInitializationEvent event) {
        logger = event.getModLog();
        logger.info("Loaded the EnderDevelopment 1.12.2 pack marker.");
    }
}
